





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Xor extends RepositoryConcept {






    private List<ISO20022_MessageBuildingBlock> iso20022_messagebuildingblocks;




    private List<ISO20022_MessageElement> iso20022_messageelements;


    public ISO20022_Xor(
    ) {
        super(
        );
        this.iso20022_messagebuildingblocks = new ArrayList<>();
        this.iso20022_messageelements = new ArrayList<>();
    }

    public ISO20022_Xor(
        ArrayList<ISO20022_MessageBuildingBlock> iso20022_messagebuildingblocks,        ArrayList<ISO20022_MessageElement> iso20022_messageelements    ) {
        this.iso20022_messagebuildingblocks = iso20022_messagebuildingblocks;
        this.iso20022_messageelements = iso20022_messageelements;
    }


    public List<ISO20022_MessageBuildingBlock> getIso20022_messagebuildingblocks() {
        return iso20022_messagebuildingblocks;
    }

    public void addIso20022_messagebuildingblock(Iso20022_messagebuildingblock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblocks.add(iso20022_messagebuildingblock);
    }
    public List<ISO20022_MessageElement> getIso20022_messageelements() {
        return iso20022_messageelements;
    }

    public void addIso20022_messageelement(Iso20022_messageelement iso20022_messageelement) {
        this.iso20022_messageelements.add(iso20022_messageelement);
    }

}