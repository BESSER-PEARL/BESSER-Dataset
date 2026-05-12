





import java.util.List;
import java.util.ArrayList;

public class services  {

    private String location;
    private String database;





    private List<company> companys;


    public services(
        String location,        String database    ) {
        this.location = location;
        this.database = database;
        this.companys = new ArrayList<>();
    }

    public services(
        String location,        String database        ArrayList<company> companys    ) {
        this.location = location;
        this.database = database;
        this.companys = companys;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }

    public List<company> getCompanys() {
        return companys;
    }

    public void addCompany(Company company) {
        this.companys.add(company);
    }

}