





import java.util.List;
import java.util.ArrayList;

public class Package_Comment  {

    private String text;
    private String user_id;
    private String id;





    private Package_Bill package_bill;


    public Package_Comment(
        String text,        String user_id,        String id    ) {
        this.text = text;
        this.user_id = user_id;
        this.id = id;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Package_Bill getPackage_bill() {
        return package_bill;
    }

    public void setPackage_bill(Package_Bill package_bill) {
        this.package_bill = package_bill;
    }

}