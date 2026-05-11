





import java.util.List;
import java.util.ArrayList;

public class customerDsl_Customer  {

    private String name;
    private String fullName;





    private customerDsl_CustomerDb customerdsl_customerdb;


    public customerDsl_Customer(
        String name,        String fullName    ) {
        this.name = name;
        this.fullName = fullName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public customerDsl_CustomerDb getCustomerdsl_customerdb() {
        return customerdsl_customerdb;
    }

    public void setCustomerdsl_customerdb(customerDsl_CustomerDb customerdsl_customerdb) {
        this.customerdsl_customerdb = customerdsl_customerdb;
    }

}