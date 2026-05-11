





import java.util.List;
import java.util.ArrayList;

public class data_IndoorLocation extends MetaInformation {

    private String name;





    private data_Location data_location;




    private data_IndoorLocation data_indoorlocation;




    private List<data_IndoorLocation> data_indoorlocations;




    private data_Location data_location;


    public data_IndoorLocation(
        String name    ) {
        super(
        );
        this.name = name;
        this.data_indoorlocations = new ArrayList<>();
    }

    public data_IndoorLocation(
        String name        ArrayList<data_IndoorLocation> data_indoorlocations    ) {
        this.name = name;
        this.data_indoorlocations = data_indoorlocations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public data_Location getData_location() {
        return data_location;
    }

    public void setData_location(data_Location data_location) {
        this.data_location = data_location;
    }
    public data_IndoorLocation getData_indoorlocation() {
        return data_indoorlocation;
    }

    public void setData_indoorlocation(data_IndoorLocation data_indoorlocation) {
        this.data_indoorlocation = data_indoorlocation;
    }
    public List<data_IndoorLocation> getData_indoorlocations() {
        return data_indoorlocations;
    }

    public void addData_indoorlocation(Data_indoorlocation data_indoorlocation) {
        this.data_indoorlocations.add(data_indoorlocation);
    }
    public data_Location getData_location() {
        return data_location;
    }

    public void setData_location(data_Location data_location) {
        this.data_location = data_location;
    }

}