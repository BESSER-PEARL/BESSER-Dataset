





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageComponentType extends TopLevelDictionaryEntry, LogicalType, MessageConcept {

    private boolean isTechnical;





    private iso20022_MessageBuildingBlock iso20022_messagebuildingblock;




    private iso20022_BusinessComponent iso20022_businesscomponent;




    private List<iso20022_MessageBuildingBlock> iso20022_messagebuildingblocks;




    private iso20022_BusinessComponent iso20022_businesscomponent;


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

    public iso20022_MessageBuildingBlock getIso20022_messagebuildingblock() {
        return iso20022_messagebuildingblock;
    }

    public void setIso20022_messagebuildingblock(iso20022_MessageBuildingBlock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblock = iso20022_messagebuildingblock;
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }
    public List<iso20022_MessageBuildingBlock> getIso20022_messagebuildingblocks() {
        return iso20022_messagebuildingblocks;
    }

    public void addIso20022_messagebuildingblock(Iso20022_messagebuildingblock iso20022_messagebuildingblock) {
        this.iso20022_messagebuildingblocks.add(iso20022_messagebuildingblock);
    }
    public iso20022_BusinessComponent getIso20022_businesscomponent() {
        return iso20022_businesscomponent;
    }

    public void setIso20022_businesscomponent(iso20022_BusinessComponent iso20022_businesscomponent) {
        this.iso20022_businesscomponent = iso20022_businesscomponent;
    }

}