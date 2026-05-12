





import java.util.List;
import java.util.ArrayList;

public class Tag  {

    private int id;
    private String color;
    private String name;





    private List<Company> companys;




    private List<Contact> contacts;


    public Tag(
        int id,        String color,        String name    ) {
        this.id = id;
        this.color = color;
        this.name = name;
        this.companys = new ArrayList<>();
        this.contacts = new ArrayList<>();
    }

    public Tag(
        int id,        String color,        String name        ArrayList<Company> companys,        ArrayList<Contact> contacts    ) {
        this.id = id;
        this.color = color;
        this.name = name;
        this.companys = companys;
        this.contacts = contacts;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Company> getCompanys() {
        return companys;
    }

    public void addCompany(Company company) {
        this.companys.add(company);
    }
    public List<Contact> getContacts() {
        return contacts;
    }

    public void addContact(Contact contact) {
        this.contacts.add(contact);
    }

}