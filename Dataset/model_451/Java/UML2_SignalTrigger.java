





import java.util.List;
import java.util.ArrayList;

public class UML2_SignalTrigger extends MessageTrigger {






    private List<UML2_Signal> uml2_signals;


    public UML2_SignalTrigger(
    ) {
        super(
        );
        this.uml2_signals = new ArrayList<>();
    }

    public UML2_SignalTrigger(
        ArrayList<UML2_Signal> uml2_signals    ) {
        this.uml2_signals = uml2_signals;
    }


    public List<UML2_Signal> getUml2_signals() {
        return uml2_signals;
    }

    public void addUml2_signal(Uml2_signal uml2_signal) {
        this.uml2_signals.add(uml2_signal);
    }

}