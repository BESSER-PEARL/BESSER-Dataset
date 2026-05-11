





import java.util.List;
import java.util.ArrayList;

public class source_ClassDiagram  {






    private List<source_PrimitiveDataType> source_primitivedatatypes;




    private List<source_Class> source_classs;




    private List<source_Association> source_associations;


    public source_ClassDiagram(
    ) {
        this.source_primitivedatatypes = new ArrayList<>();
        this.source_classs = new ArrayList<>();
        this.source_associations = new ArrayList<>();
    }

    public source_ClassDiagram(
        ArrayList<source_PrimitiveDataType> source_primitivedatatypes,        ArrayList<source_Class> source_classs,        ArrayList<source_Association> source_associations    ) {
        this.source_primitivedatatypes = source_primitivedatatypes;
        this.source_classs = source_classs;
        this.source_associations = source_associations;
    }


    public List<source_PrimitiveDataType> getSource_primitivedatatypes() {
        return source_primitivedatatypes;
    }

    public void addSource_primitivedatatype(Source_primitivedatatype source_primitivedatatype) {
        this.source_primitivedatatypes.add(source_primitivedatatype);
    }
    public List<source_Class> getSource_classs() {
        return source_classs;
    }

    public void addSource_class(Source_class source_class) {
        this.source_classs.add(source_class);
    }
    public List<source_Association> getSource_associations() {
        return source_associations;
    }

    public void addSource_association(Source_association source_association) {
        this.source_associations.add(source_association);
    }

}