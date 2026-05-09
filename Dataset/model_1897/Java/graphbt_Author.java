





import java.util.List;
import java.util.ArrayList;

public class graphbt_Author  {

    private String name;
    private String contact;
    private String role;





    private graphbt_AuthorList graphbt_authorlist;


    public graphbt_Author(
        String name,        String contact,        String role    ) {
        this.name = name;
        this.contact = contact;
        this.role = role;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public graphbt_AuthorList getGraphbt_authorlist() {
        return graphbt_authorlist;
    }

    public void setGraphbt_authorlist(graphbt_AuthorList graphbt_authorlist) {
        this.graphbt_authorlist = graphbt_authorlist;
    }

}