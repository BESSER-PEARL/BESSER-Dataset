





import java.util.List;
import java.util.ArrayList;

public class data_Organisation extends InformationObject {






    private List<data_Organisation> data_organisations;




    private data_Organisation data_organisation;


    public data_Organisation(
    ) {
        super(
        );
        this.data_organisations = new ArrayList<>();
    }

    public data_Organisation(
        ArrayList<data_Organisation> data_organisations    ) {
        this.data_organisations = data_organisations;
    }


    public List<data_Organisation> getData_organisations() {
        return data_organisations;
    }

    public void addData_organisation(Data_organisation data_organisation) {
        this.data_organisations.add(data_organisation);
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
    }

}