





import java.util.List;
import java.util.ArrayList;

public class mngr_ManagerParameter extends NamedElement {

    private boolean isInput;
    private String LitteralString;
    private int LitteralInteger;
    private float LitteralUnlimitedNatural;
    private boolean LitteralBoolean;





    private mngr_Manager mngr_manager;




    private List<mngr_ManagerState> mngr_managerstates;




    private mngr_ManagerState mngr_managerstate;




    private mngr_Manager mngr_manager;


    public mngr_ManagerParameter(
        boolean isInput,        String LitteralString,        int LitteralInteger,        float LitteralUnlimitedNatural,        boolean LitteralBoolean    ) {
        super(
        );
        this.isInput = isInput;
        this.LitteralString = LitteralString;
        this.LitteralInteger = LitteralInteger;
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
        this.LitteralBoolean = LitteralBoolean;
        this.mngr_managerstates = new ArrayList<>();
    }

    public mngr_ManagerParameter(
        boolean isInput,        String LitteralString,        int LitteralInteger,        float LitteralUnlimitedNatural,        boolean LitteralBoolean        ArrayList<mngr_ManagerState> mngr_managerstates    ) {
        this.isInput = isInput;
        this.LitteralString = LitteralString;
        this.LitteralInteger = LitteralInteger;
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
        this.LitteralBoolean = LitteralBoolean;
        this.mngr_managerstates = mngr_managerstates;
    }

    public boolean getIsinput() {
        return isInput;
    }

    public void setIsinput(boolean isInput) {
        this.isInput = isInput;
    }
    public String getLitteralstring() {
        return LitteralString;
    }

    public void setLitteralstring(String LitteralString) {
        this.LitteralString = LitteralString;
    }
    public int getLitteralinteger() {
        return LitteralInteger;
    }

    public void setLitteralinteger(int LitteralInteger) {
        this.LitteralInteger = LitteralInteger;
    }
    public float getLitteralunlimitednatural() {
        return LitteralUnlimitedNatural;
    }

    public void setLitteralunlimitednatural(float LitteralUnlimitedNatural) {
        this.LitteralUnlimitedNatural = LitteralUnlimitedNatural;
    }
    public boolean getLitteralboolean() {
        return LitteralBoolean;
    }

    public void setLitteralboolean(boolean LitteralBoolean) {
        this.LitteralBoolean = LitteralBoolean;
    }

    public mngr_Manager getMngr_manager() {
        return mngr_manager;
    }

    public void setMngr_manager(mngr_Manager mngr_manager) {
        this.mngr_manager = mngr_manager;
    }
    public List<mngr_ManagerState> getMngr_managerstates() {
        return mngr_managerstates;
    }

    public void addMngr_managerstate(Mngr_managerstate mngr_managerstate) {
        this.mngr_managerstates.add(mngr_managerstate);
    }
    public mngr_ManagerState getMngr_managerstate() {
        return mngr_managerstate;
    }

    public void setMngr_managerstate(mngr_ManagerState mngr_managerstate) {
        this.mngr_managerstate = mngr_managerstate;
    }
    public mngr_Manager getMngr_manager() {
        return mngr_manager;
    }

    public void setMngr_manager(mngr_Manager mngr_manager) {
        this.mngr_manager = mngr_manager;
    }

}