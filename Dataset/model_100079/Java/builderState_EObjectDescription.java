





import java.util.List;
import java.util.ArrayList;

public class builderState_EObjectDescription extends IEObjectDescription {

    private String fragment;





    private List<builderState_UserDataEntry> builderstate_userdataentrys;


    public builderState_EObjectDescription(
        String fragment    ) {
        super(
        );
        this.fragment = fragment;
        this.builderstate_userdataentrys = new ArrayList<>();
    }

    public builderState_EObjectDescription(
        String fragment        ArrayList<builderState_UserDataEntry> builderstate_userdataentrys    ) {
        this.fragment = fragment;
        this.builderstate_userdataentrys = builderstate_userdataentrys;
    }

    public String getFragment() {
        return fragment;
    }

    public void setFragment(String fragment) {
        this.fragment = fragment;
    }

    public List<builderState_UserDataEntry> getBuilderstate_userdataentrys() {
        return builderstate_userdataentrys;
    }

    public void addBuilderstate_userdataentry(Builderstate_userdataentry builderstate_userdataentry) {
        this.builderstate_userdataentrys.add(builderstate_userdataentry);
    }

}