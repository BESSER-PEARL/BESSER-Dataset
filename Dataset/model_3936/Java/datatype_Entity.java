





import java.util.List;
import java.util.ArrayList;

public class datatype_Entity extends Type {






    private List<datatype_Property> datatype_propertys;




    private datatype_Entity datatype_entity;


    public datatype_Entity(
    ) {
        super(
        );
        this.datatype_propertys = new ArrayList<>();
    }

    public datatype_Entity(
        ArrayList<datatype_Property> datatype_propertys    ) {
        this.datatype_propertys = datatype_propertys;
    }


    public List<datatype_Property> getDatatype_propertys() {
        return datatype_propertys;
    }

    public void addDatatype_property(Datatype_property datatype_property) {
        this.datatype_propertys.add(datatype_property);
    }
    public datatype_Entity getDatatype_entity() {
        return datatype_entity;
    }

    public void setDatatype_entity(datatype_Entity datatype_entity) {
        this.datatype_entity = datatype_entity;
    }

}