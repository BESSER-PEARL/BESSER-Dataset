





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMTransitionWithState extends FSMTransition {






    private List<StringToIntegerMap> stringtointegermaps;


    public analysis_scheduling_FSMTransitionWithState(
    ) {
        super(
        );
        this.stringtointegermaps = new ArrayList<>();
    }

    public analysis_scheduling_FSMTransitionWithState(
        ArrayList<StringToIntegerMap> stringtointegermaps    ) {
        this.stringtointegermaps = stringtointegermaps;
    }


    public List<StringToIntegerMap> getStringtointegermaps() {
        return stringtointegermaps;
    }

    public void addStringtointegermap(Stringtointegermap stringtointegermap) {
        this.stringtointegermaps.add(stringtointegermap);
    }

}