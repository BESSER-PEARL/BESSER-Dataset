





import java.util.List;
import java.util.ArrayList;

public class megal_MegalEntity extends MegalNamed {

    private boolean many;





    private megal_MegalLink megal_megallink;




    private megal_MegalLink megal_megallink;




    private megal_MegalLink megal_megallink;




    private List<megal_MegalEntity> megal_megalentitys;


    public megal_MegalEntity(
        boolean many    ) {
        super(
        );
        this.many = many;
        this.megal_megalentitys = new ArrayList<>();
    }

    public megal_MegalEntity(
        boolean many        ArrayList<megal_MegalEntity> megal_megalentitys    ) {
        this.many = many;
        this.megal_megalentitys = megal_megalentitys;
    }

    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public megal_MegalLink getMegal_megallink() {
        return megal_megallink;
    }

    public void setMegal_megallink(megal_MegalLink megal_megallink) {
        this.megal_megallink = megal_megallink;
    }
    public megal_MegalLink getMegal_megallink() {
        return megal_megallink;
    }

    public void setMegal_megallink(megal_MegalLink megal_megallink) {
        this.megal_megallink = megal_megallink;
    }
    public megal_MegalLink getMegal_megallink() {
        return megal_megallink;
    }

    public void setMegal_megallink(megal_MegalLink megal_megallink) {
        this.megal_megallink = megal_megallink;
    }
    public List<megal_MegalEntity> getMegal_megalentitys() {
        return megal_megalentitys;
    }

    public void addMegal_megalentity(Megal_megalentity megal_megalentity) {
        this.megal_megalentitys.add(megal_megalentity);
    }

}