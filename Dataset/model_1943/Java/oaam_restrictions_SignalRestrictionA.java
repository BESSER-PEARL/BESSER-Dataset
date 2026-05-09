





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_SignalRestrictionA  {






    private List<Signal> signals;


    public oaam_restrictions_SignalRestrictionA(
    ) {
        this.signals = new ArrayList<>();
    }

    public oaam_restrictions_SignalRestrictionA(
        ArrayList<Signal> signals    ) {
        this.signals = signals;
    }


    public List<Signal> getSignals() {
        return signals;
    }

    public void addSignal(Signal signal) {
        this.signals.add(signal);
    }

}