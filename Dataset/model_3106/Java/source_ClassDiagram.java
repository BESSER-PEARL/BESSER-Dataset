





import java.util.List;
import java.util.ArrayList;

public class source_ClassDiagram  {






    private List<source_PrimitiveDataType> source_primitivedatatypes;


    public source_ClassDiagram(
    ) {
        this.source_primitivedatatypes = new ArrayList<>();
    }

    public source_ClassDiagram(
        ArrayList<source_PrimitiveDataType> source_primitivedatatypes    ) {
        this.source_primitivedatatypes = source_primitivedatatypes;
    }


    public List<source_PrimitiveDataType> getSource_primitivedatatypes() {
        return source_primitivedatatypes;
    }

    public void addSource_primitivedatatype(Source_primitivedatatype source_primitivedatatype) {
        this.source_primitivedatatypes.add(source_primitivedatatype);
    }

}