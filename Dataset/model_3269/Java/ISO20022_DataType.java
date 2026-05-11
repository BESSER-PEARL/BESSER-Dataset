





import java.util.List;
import java.util.ArrayList;

public class ISO20022_DataType extends LogicalType, BusinessElementType, TopLevelDictionaryEntry {






    private ISO20022_MessageBuildingBlock iso20022_messagebuildingblock;




    private List<ISO20022_Facet> iso20022_facets;




    private ISO20022_MessageAttribute iso20022_messageattribute;


    public ISO20022_DataType(
    ) {
        super(
        );
        this.iso20022_facets = new ArrayList<>();
    }

    public ISO20022_DataType(
        ArrayList<ISO20022_Facet> iso20022_facets    ) {
        this.iso20022_facets = iso20022_facets;
    }


    public ISO20022_MessageBuildingBlock getIso20022_messagebuildingblock() {
        return iso20022_messagebuildingblock;
    }

    public void setIso20022_messagebuildingblock(ISO20022_MessageBuildingBlock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblock = iso20022_messagebuildingblock;
    }
    public List<ISO20022_Facet> getIso20022_facets() {
        return iso20022_facets;
    }

    public void addIso20022_facet(Iso20022_facet iso20022_facet) {
        this.iso20022_facets.add(iso20022_facet);
    }
    public ISO20022_MessageAttribute getIso20022_messageattribute() {
        return iso20022_messageattribute;
    }

    public void setIso20022_messageattribute(ISO20022_MessageAttribute iso20022_messageattribute) {
        this.iso20022_messageattribute = iso20022_messageattribute;
    }

}