





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_SignalGroupRestrictionA  {






    private List<SignalGroup> signalgroups;


    public oaam_restrictions_SignalGroupRestrictionA(
    ) {
        this.signalgroups = new ArrayList<>();
    }

    public oaam_restrictions_SignalGroupRestrictionA(
        ArrayList<SignalGroup> signalgroups    ) {
        this.signalgroups = signalgroups;
    }


    public List<SignalGroup> getSignalgroups() {
        return signalgroups;
    }

    public void addSignalgroup(Signalgroup signalgroup) {
        this.signalgroups.add(signalgroup);
    }

}