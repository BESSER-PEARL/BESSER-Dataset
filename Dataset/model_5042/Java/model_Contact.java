




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Contact extends IEntity {

    private String contactType;
    private String webshopName;
    private String title;
    private String supplierNumber;
    private String useNetGross;
    private String company;
    private String discount;
    private String firstName;
    private String note;
    private String customerNumber;
    private String fax;
    private String useSalesEqualizationTax;
    private String website;
    private String phone;
    private LocalDate birthday;
    private String email;
    private String vatNumber;
    private String mobile;
    private String gln;
    private String reliability;
    private String mandateReference;
    private String vatNumberValid;
    private String gender;





    private model_Document model_document;




    private model_Address model_address;




    private model_BankAccount model_bankaccount;




    private model_Payment model_payment;




    private model_Contact model_contact;




    private model_ContactCategory model_contactcategory;




    private model_Document model_document;


    public model_Contact(
        String contactType,        String webshopName,        String title,        String supplierNumber,        String useNetGross,        String company,        String discount,        String firstName,        String note,        String customerNumber,        String fax,        String useSalesEqualizationTax,        String website,        String phone,        LocalDate birthday,        String email,        String vatNumber,        String mobile,        String gln,        String reliability,        String mandateReference,        String vatNumberValid,        String gender    ) {
        super(
        );
        this.contactType = contactType;
        this.webshopName = webshopName;
        this.title = title;
        this.supplierNumber = supplierNumber;
        this.useNetGross = useNetGross;
        this.company = company;
        this.discount = discount;
        this.firstName = firstName;
        this.note = note;
        this.customerNumber = customerNumber;
        this.fax = fax;
        this.useSalesEqualizationTax = useSalesEqualizationTax;
        this.website = website;
        this.phone = phone;
        this.birthday = birthday;
        this.email = email;
        this.vatNumber = vatNumber;
        this.mobile = mobile;
        this.gln = gln;
        this.reliability = reliability;
        this.mandateReference = mandateReference;
        this.vatNumberValid = vatNumberValid;
        this.gender = gender;
    }


    public String getContacttype() {
        return contactType;
    }

    public void setContacttype(String contactType) {
        this.contactType = contactType;
    }
    public String getWebshopname() {
        return webshopName;
    }

    public void setWebshopname(String webshopName) {
        this.webshopName = webshopName;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getSuppliernumber() {
        return supplierNumber;
    }

    public void setSuppliernumber(String supplierNumber) {
        this.supplierNumber = supplierNumber;
    }
    public String getUsenetgross() {
        return useNetGross;
    }

    public void setUsenetgross(String useNetGross) {
        this.useNetGross = useNetGross;
    }
    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }
    public String getDiscount() {
        return discount;
    }

    public void setDiscount(String discount) {
        this.discount = discount;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getCustomernumber() {
        return customerNumber;
    }

    public void setCustomernumber(String customerNumber) {
        this.customerNumber = customerNumber;
    }
    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
    }
    public String getUsesalesequalizationtax() {
        return useSalesEqualizationTax;
    }

    public void setUsesalesequalizationtax(String useSalesEqualizationTax) {
        this.useSalesEqualizationTax = useSalesEqualizationTax;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public LocalDate getBirthday() {
        return birthday;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getVatnumber() {
        return vatNumber;
    }

    public void setVatnumber(String vatNumber) {
        this.vatNumber = vatNumber;
    }
    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }
    public String getGln() {
        return gln;
    }

    public void setGln(String gln) {
        this.gln = gln;
    }
    public String getReliability() {
        return reliability;
    }

    public void setReliability(String reliability) {
        this.reliability = reliability;
    }
    public String getMandatereference() {
        return mandateReference;
    }

    public void setMandatereference(String mandateReference) {
        this.mandateReference = mandateReference;
    }
    public String getVatnumbervalid() {
        return vatNumberValid;
    }

    public void setVatnumbervalid(String vatNumberValid) {
        this.vatNumberValid = vatNumberValid;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public model_Document getModel_document() {
        return model_document;
    }

    public void setModel_document(model_Document model_document) {
        this.model_document = model_document;
    }
    public model_Address getModel_address() {
        return model_address;
    }

    public void setModel_address(model_Address model_address) {
        this.model_address = model_address;
    }
    public model_BankAccount getModel_bankaccount() {
        return model_bankaccount;
    }

    public void setModel_bankaccount(model_BankAccount model_bankaccount) {
        this.model_bankaccount = model_bankaccount;
    }
    public model_Payment getModel_payment() {
        return model_payment;
    }

    public void setModel_payment(model_Payment model_payment) {
        this.model_payment = model_payment;
    }
    public model_Contact getModel_contact() {
        return model_contact;
    }

    public void setModel_contact(model_Contact model_contact) {
        this.model_contact = model_contact;
    }
    public model_ContactCategory getModel_contactcategory() {
        return model_contactcategory;
    }

    public void setModel_contactcategory(model_ContactCategory model_contactcategory) {
        this.model_contactcategory = model_contactcategory;
    }
    public model_Document getModel_document() {
        return model_document;
    }

    public void setModel_document(model_Document model_document) {
        this.model_document = model_document;
    }

}