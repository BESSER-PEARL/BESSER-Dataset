





import java.util.List;
import java.util.ArrayList;

public class megal_MegalRelationshipType extends MegalNamed {

    private boolean leftMany;
    private boolean rightBoth;
    private boolean rightMany;
    private boolean leftBoth;





    private megal_MegalEntityType megal_megalentitytype;




    private List<megal_MegalEntity> megal_megalentitys;




    private List<megal_MegalEntity> megal_megalentitys;




    private megal_MegalEntityType megal_megalentitytype;


    public megal_MegalRelationshipType(
        boolean leftMany,        boolean rightBoth,        boolean rightMany,        boolean leftBoth    ) {
        super(
        );
        this.leftMany = leftMany;
        this.rightBoth = rightBoth;
        this.rightMany = rightMany;
        this.leftBoth = leftBoth;
        this.megal_megalentitys = new ArrayList<>();
        this.megal_megalentitys = new ArrayList<>();
    }

    public megal_MegalRelationshipType(
        boolean leftMany,        boolean rightBoth,        boolean rightMany,        boolean leftBoth        ArrayList<megal_MegalEntity> megal_megalentitys,        ArrayList<megal_MegalEntity> megal_megalentitys    ) {
        this.leftMany = leftMany;
        this.rightBoth = rightBoth;
        this.rightMany = rightMany;
        this.leftBoth = leftBoth;
        this.megal_megalentitys = megal_megalentitys;
        this.megal_megalentitys = megal_megalentitys;
    }

    public boolean getLeftmany() {
        return leftMany;
    }

    public void setLeftmany(boolean leftMany) {
        this.leftMany = leftMany;
    }
    public boolean getRightboth() {
        return rightBoth;
    }

    public void setRightboth(boolean rightBoth) {
        this.rightBoth = rightBoth;
    }
    public boolean getRightmany() {
        return rightMany;
    }

    public void setRightmany(boolean rightMany) {
        this.rightMany = rightMany;
    }
    public boolean getLeftboth() {
        return leftBoth;
    }

    public void setLeftboth(boolean leftBoth) {
        this.leftBoth = leftBoth;
    }

    public megal_MegalEntityType getMegal_megalentitytype() {
        return megal_megalentitytype;
    }

    public void setMegal_megalentitytype(megal_MegalEntityType megal_megalentitytype) {
        this.megal_megalentitytype = megal_megalentitytype;
    }
    public List<megal_MegalEntity> getMegal_megalentitys() {
        return megal_megalentitys;
    }

    public void addMegal_megalentity(Megal_megalentity megal_megalentity) {
        this.megal_megalentitys.add(megal_megalentity);
    }
    public List<megal_MegalEntity> getMegal_megalentitys() {
        return megal_megalentitys;
    }

    public void addMegal_megalentity(Megal_megalentity megal_megalentity) {
        this.megal_megalentitys.add(megal_megalentity);
    }
    public megal_MegalEntityType getMegal_megalentitytype() {
        return megal_megalentitytype;
    }

    public void setMegal_megalentitytype(megal_MegalEntityType megal_megalentitytype) {
        this.megal_megalentitytype = megal_megalentitytype;
    }

}