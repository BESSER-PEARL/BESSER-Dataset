




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Company  {

    private String linkedin_url;
    private String city;
    private String website;
    private String description;
    private None industry;
    private String phone;
    private LocalDateTime updated_at;
    private int id;
    private String address;
    private String name;
    private String country;
    private LocalDateTime created_at;
    private None size;





    private List<Contact> contacts;




    private List<Opportunity> opportunitys;


    public Company(
        String linkedin_url,        String city,        String website,        String description,        None industry,        String phone,        LocalDateTime updated_at,        int id,        String address,        String name,        String country,        LocalDateTime created_at,        None size    ) {
        this.linkedin_url = linkedin_url;
        this.city = city;
        this.website = website;
        this.description = description;
        this.industry = industry;
        this.phone = phone;
        this.updated_at = updated_at;
        this.id = id;
        this.address = address;
        this.name = name;
        this.country = country;
        this.created_at = created_at;
        this.size = size;
        this.contacts = new ArrayList<>();
        this.opportunitys = new ArrayList<>();
    }

    public Company(
        String linkedin_url,        String city,        String website,        String description,        None industry,        String phone,        LocalDateTime updated_at,        int id,        String address,        String name,        String country,        LocalDateTime created_at,        None size        ArrayList<Contact> contacts,        ArrayList<Opportunity> opportunitys    ) {
        this.linkedin_url = linkedin_url;
        this.city = city;
        this.website = website;
        this.description = description;
        this.industry = industry;
        this.phone = phone;
        this.updated_at = updated_at;
        this.id = id;
        this.address = address;
        this.name = name;
        this.country = country;
        this.created_at = created_at;
        this.size = size;
        this.contacts = contacts;
        this.opportunitys = opportunitys;
    }

    public String getLinkedin_url() {
        return linkedin_url;
    }

    public void setLinkedin_url(String linkedin_url) {
        this.linkedin_url = linkedin_url;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getIndustry() {
        return industry;
    }

    public void setIndustry(None industry) {
        this.industry = industry;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public LocalDateTime getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(LocalDateTime updated_at) {
        this.updated_at = updated_at;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public None getSize() {
        return size;
    }

    public void setSize(None size) {
        this.size = size;
    }

    public List<Contact> getContacts() {
        return contacts;
    }

    public void addContact(Contact contact) {
        this.contacts.add(contact);
    }
    public List<Opportunity> getOpportunitys() {
        return opportunitys;
    }

    public void addOpportunity(Opportunity opportunity) {
        this.opportunitys.add(opportunity);
    }

}