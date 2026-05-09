





import java.util.List;
import java.util.ArrayList;

public class mvc_MvcApplication  {

    private String name;
    private String picture;
    private String description;
    private String email;
    private String pagelink;



    public mvc_MvcApplication(
        String name,        String picture,        String description,        String email,        String pagelink    ) {
        this.name = name;
        this.picture = picture;
        this.description = description;
        this.email = email;
        this.pagelink = pagelink;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPagelink() {
        return pagelink;
    }

    public void setPagelink(String pagelink) {
        this.pagelink = pagelink;
    }


}