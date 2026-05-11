





import java.util.List;
import java.util.ArrayList;

public class commons_PostalAddress extends SchemaVersionable, Identifiable, NameContainer {

    private String primaryPhone;
    private String schemaVersion;
    private String province;
    private String primaryWorkPhone;
    private String description;
    private boolean primaryShipping;
    private String country;
    private String street;
    private String mobiles;
    private String organization;
    private String primaryHomePhone;
    private String primaryEmail;
    private String homePhones;
    private String postalCode;
    private String primaryMobile;
    private String countryCode;
    private String emails;
    private String phones;
    private String validationTime;
    private boolean primary;
    private String city;
    private String district;
    private boolean primaryBilling;
    private String jneAreaCode;
    private String workPhones;



    public commons_PostalAddress(
        String primaryPhone,        String schemaVersion,        String province,        String primaryWorkPhone,        String description,        boolean primaryShipping,        String country,        String street,        String mobiles,        String organization,        String primaryHomePhone,        String primaryEmail,        String homePhones,        String postalCode,        String primaryMobile,        String countryCode,        String emails,        String phones,        String validationTime,        boolean primary,        String city,        String district,        boolean primaryBilling,        String jneAreaCode,        String workPhones    ) {
        super(
        );
        this.primaryPhone = primaryPhone;
        this.schemaVersion = schemaVersion;
        this.province = province;
        this.primaryWorkPhone = primaryWorkPhone;
        this.description = description;
        this.primaryShipping = primaryShipping;
        this.country = country;
        this.street = street;
        this.mobiles = mobiles;
        this.organization = organization;
        this.primaryHomePhone = primaryHomePhone;
        this.primaryEmail = primaryEmail;
        this.homePhones = homePhones;
        this.postalCode = postalCode;
        this.primaryMobile = primaryMobile;
        this.countryCode = countryCode;
        this.emails = emails;
        this.phones = phones;
        this.validationTime = validationTime;
        this.primary = primary;
        this.city = city;
        this.district = district;
        this.primaryBilling = primaryBilling;
        this.jneAreaCode = jneAreaCode;
        this.workPhones = workPhones;
    }


    public String getPrimaryphone() {
        return primaryPhone;
    }

    public void setPrimaryphone(String primaryPhone) {
        this.primaryPhone = primaryPhone;
    }
    public String getSchemaversion() {
        return schemaVersion;
    }

    public void setSchemaversion(String schemaVersion) {
        this.schemaVersion = schemaVersion;
    }
    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }
    public String getPrimaryworkphone() {
        return primaryWorkPhone;
    }

    public void setPrimaryworkphone(String primaryWorkPhone) {
        this.primaryWorkPhone = primaryWorkPhone;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getPrimaryshipping() {
        return primaryShipping;
    }

    public void setPrimaryshipping(boolean primaryShipping) {
        this.primaryShipping = primaryShipping;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getMobiles() {
        return mobiles;
    }

    public void setMobiles(String mobiles) {
        this.mobiles = mobiles;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getPrimaryhomephone() {
        return primaryHomePhone;
    }

    public void setPrimaryhomephone(String primaryHomePhone) {
        this.primaryHomePhone = primaryHomePhone;
    }
    public String getPrimaryemail() {
        return primaryEmail;
    }

    public void setPrimaryemail(String primaryEmail) {
        this.primaryEmail = primaryEmail;
    }
    public String getHomephones() {
        return homePhones;
    }

    public void setHomephones(String homePhones) {
        this.homePhones = homePhones;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getPrimarymobile() {
        return primaryMobile;
    }

    public void setPrimarymobile(String primaryMobile) {
        this.primaryMobile = primaryMobile;
    }
    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }
    public String getEmails() {
        return emails;
    }

    public void setEmails(String emails) {
        this.emails = emails;
    }
    public String getPhones() {
        return phones;
    }

    public void setPhones(String phones) {
        this.phones = phones;
    }
    public String getValidationtime() {
        return validationTime;
    }

    public void setValidationtime(String validationTime) {
        this.validationTime = validationTime;
    }
    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }
    public boolean getPrimarybilling() {
        return primaryBilling;
    }

    public void setPrimarybilling(boolean primaryBilling) {
        this.primaryBilling = primaryBilling;
    }
    public String getJneareacode() {
        return jneAreaCode;
    }

    public void setJneareacode(String jneAreaCode) {
        this.jneAreaCode = jneAreaCode;
    }
    public String getWorkphones() {
        return workPhones;
    }

    public void setWorkphones(String workPhones) {
        this.workPhones = workPhones;
    }


}