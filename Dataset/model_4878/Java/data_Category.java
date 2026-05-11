





import java.util.List;
import java.util.ArrayList;

public class data_Category extends Classification {






    private data_Category data_category;




    private data_InformationObject data_informationobject;




    private data_Category data_category;




    private List<data_InformationObject> data_informationobjects;




    private data_InformationObject data_informationobject;




    private List<data_InformationObject> data_informationobjects;


    public data_Category(
    ) {
        super(
        );
        this.data_informationobjects = new ArrayList<>();
        this.data_informationobjects = new ArrayList<>();
    }

    public data_Category(
        ArrayList<data_InformationObject> data_informationobjects,        ArrayList<data_InformationObject> data_informationobjects    ) {
        this.data_informationobjects = data_informationobjects;
        this.data_informationobjects = data_informationobjects;
    }


    public data_Category getData_category() {
        return data_category;
    }

    public void setData_category(data_Category data_category) {
        this.data_category = data_category;
    }
    public data_InformationObject getData_informationobject() {
        return data_informationobject;
    }

    public void setData_informationobject(data_InformationObject data_informationobject) {
        this.data_informationobject = data_informationobject;
    }
    public data_Category getData_category() {
        return data_category;
    }

    public void setData_category(data_Category data_category) {
        this.data_category = data_category;
    }
    public List<data_InformationObject> getData_informationobjects() {
        return data_informationobjects;
    }

    public void addData_informationobject(Data_informationobject data_informationobject) {
        this.data_informationobjects.add(data_informationobject);
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