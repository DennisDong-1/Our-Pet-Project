from django.db import models
from django.conf import settings

# Create your models here.

class RehomerProfile(models.Model):
    # Linking the profile to a user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rehomer_profile')
    
    # Fields specific to adopter
    bio = models.TextField(blank=True, null=True)
    rehome_history = models.BooleanField(default=False)  # Indicates previous Rehomer experience
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

class RehomerApplication(models.Model):
    # Foreign keys to link adopters with pets and applications
    rehomer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rehomer_applications')
    pet = models.ForeignKey('Pets.Pet', on_delete=models.CASCADE, related_name='rehomer_applications')  # assuming pets app with Pet model
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    reason = models.TextField()  # Reason the rehomers wants to rehome the pet

    def __str__(self):
        return f"Application by {self.rehomer.email} for {self.pet}"

class RehomerReference(models.Model):
    # References provided by rehomers to validate their application
    rehomer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rehomer_references')
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reference for {self.rehomer.email} - {self.name}"