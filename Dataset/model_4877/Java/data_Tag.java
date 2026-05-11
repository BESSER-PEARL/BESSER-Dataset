





import java.util.List;
import java.util.ArrayList;

public class data_Tag extends Classification {






    private data_InformationObject data_informationobject;




    private List<data_InformationObject> data_informationobjects;


    public data_Tag(
    ) {
        super(
        );
        this.data_informationobjects = new ArrayList<>();
    }

    public data_Tag(
        ArrayList<data_InformationObject> data_informationobjects    ) {
        this.data_informationobjects = data_informationobjects;
    }


    public data_InformationObject getData_informationobject() {
        return data_informationobject;
    }

    public void setData_informationobject(data_InformationObject data_informationobject) {
        this.data_informationobject = data_informationobject;
    }
    public List<data_InformationObject> getData_informationobjects() {
        return data_informationobjects;
    }

    public void addData_informationobject(Data_informationobject data_informationobject) {
        this.data_informationobjects.add(data_informationobject);
    }

}