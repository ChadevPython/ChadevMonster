# -*- coding: utf-8 -*-

from chadevmonster import db


class ModelMixin(object):

    """ Mixin class for database model helper methods/attributes.

    To enable these helpers on models, ensure to include this mixin with your
    class definition:
            class MyModel(db.Model, ModelMixin):
                # model definition
    """

    def __repr__(self):
        return f'<{self.class_name}> {self.__dict__}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Delete instance.
        """
        db.session.delete(self)
        db.session.commit()

    def deactivate(self):
        """ Deactivate an instance and update db record.
        """
        self.active = False
        self.save()

    def reactivate(self):
        """ Reactivate a deactivated instance.
        """
        self.active = True
        self.save()

    def audit(self, item, user=None, update=False, delete=False, info=None):
        """Generic audit entry on object insert.

        Audit entries for object updates are handled in views.
        """
        # generic AuditLog entry on object creation
        from smartbook.models.history import History

        if update:
            History.save_entry(self, user=user, action="{} Updated".format(self.class_name), info=info)
        elif delete:
            History.save_entry(self, user=user, action="{} Deleted".format(self.class_name), delete=True)
        else:
            History.save_entry(self, user=user, action="{} Created".format(self.class_name))

    @property
    def class_name(self):
        """Shortcut for returning class name.

        """
        return self.__class__.__name__
