




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class User  {

    private LocalDateTime created_at;
    private String first_name;
    private int id;
    private String password_hash;
    private None role;
    private LocalDateTime last_login;
    private String email;
    private String last_name;
    private boolean is_active;





    private List<Opportunity> opportunitys;




    private List<Contact> contacts;




    private List<Company> companys;


    public User(
        LocalDateTime created_at,        String first_name,        int id,        String password_hash,        None role,        LocalDateTime last_login,        String email,        String last_name,        boolean is_active    ) {
        this.created_at = created_at;
        this.first_name = first_name;
        this.id = id;
        this.password_hash = password_hash;
        this.role = role;
        this.last_login = last_login;
        this.email = email;
        this.last_name = last_name;
        this.is_active = is_active;
        this.opportunitys = new ArrayList<>();
        this.contacts = new ArrayList<>();
        this.companys = new ArrayList<>();
    }

    public User(
        LocalDateTime created_at,        String first_name,        int id,        String password_hash,        None role,        LocalDateTime last_login,        String email,        String last_name,        boolean is_active        ArrayList<Opportunity> opportunitys,        ArrayList<Contact> contacts,        ArrayList<Company> companys    ) {
        this.created_at = created_at;
        this.first_name = first_name;
        this.id = id;
        this.password_hash = password_hash;
        this.role = role;
        this.last_login = last_login;
        this.email = email;
        this.last_name = last_name;
        this.is_active = is_active;
        this.opportunitys = opportunitys;
        this.contacts = contacts;
        this.companys = companys;
    }

    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword_hash() {
        return password_hash;
    }

    public void setPassword_hash(String password_hash) {
        this.password_hash = password_hash;
    }
    public None getRole() {
        return role;
    }

    public void setRole(None role) {
        this.role = role;
    }
    public LocalDateTime getLast_login() {
        return last_login;
    }

    public void setLast_login(LocalDateTime last_login) {
        this.last_login = last_login;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public boolean getIs_active() {
        return is_active;
    }

    public void setIs_active(boolean is_active) {
        this.is_active = is_active;
    }

    public List<Opportunity> getOpportunitys() {
        return opportunitys;
    }

    public void addOpportunity(Opportunity opportunity) {
        this.opportunitys.add(opportunity);
    }
    public List<Contact> getContacts() {
        return contacts;
    }

    public void addContact(Contact contact) {
        this.contacts.add(contact);
    }
    public List<Company> getCompanys() {
        return companys;
    }

    public void addCompany(Company company) {
        this.companys.add(company);
    }

}