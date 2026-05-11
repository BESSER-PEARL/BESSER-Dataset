





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageComponentType extends LogicalType, TopLevelDictionaryEntry, MessageConcept {

    private boolean isTechnical;





    private List<iso20022_MessageBuildingBlock> iso20022_messagebuildingblocks;




    private iso20022_MessageBuildingBlock iso20022_messagebuildingblock;




    private iso20022_MessageAttribute iso20022_messageattribute;




    private iso20022_MessageAssociationEnd iso20022_messageassociationend;


    public iso20022_MessageComponentType(
        boolean isTechnical    ) {
        super(
        );
        this.isTechnical = isTechnical;
        this.iso20022_messagebuildingblocks = new ArrayList<>();
    }

    public iso20022_MessageComponentType(
        boolean isTechnical        ArrayList<iso20022_MessageBuildingBlock> iso20022_messagebuildingblocks    ) {
        this.isTechnical = isTechnical;
        this.iso20022_messagebuildingblocks = iso20022_messagebuildingblocks;
    }

    public boolean getIstechnical() {
        return isTechnical;
    }

    public void setIstechnical(boolean isTechnical) {
        this.isTechnical = isTechnical;
    }

    public List<iso20022_MessageBuildingBlock> getIso20022_messagebuildingblocks() {
        return iso20022_messagebuildingblocks;
    }

    public void addIso20022_messagebuildingblock(Iso20022_messagebuildingblock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblocks.add(iso20022_messagebuildingblock);
    }
    public iso20022_MessageBuildingBlock getIso20022_messagebuildingblock() {
        return iso20022_messagebuildingblock;
    }

    public void setIso20022_messagebuildingblock(iso20022_MessageBuildingBlock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblock = iso20022_messagebuildingblock;
    }
    public iso20022_MessageAttribute getIso20022_messageattribute() {
        return iso20022_messageattribute;
    }

    public void setIso20022_messageattribute(iso20022_MessageAttribute iso20022_messageattribute) {
        this.iso20022_messageattribute = iso20022_messageattribute;
    }
    public iso20022_MessageAssociationEnd getIso20022_messageassociationend() {
        return iso20022_messageassociationend;
    }

    public void setIso20022_messageassociationend(iso20022_MessageAssociationEnd iso20022_messageassociationend) {
        this.iso20022_messageassociationend = iso20022_messageassociationend;
    }

}