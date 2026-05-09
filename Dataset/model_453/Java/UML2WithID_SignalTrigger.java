





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_SignalTrigger extends MessageTrigger {






    private List<UML2WithID_Signal> uml2withid_signals;


    public UML2WithID_SignalTrigger(
    ) {
        super(
        );
        this.uml2withid_signals = new ArrayList<>();
    }

    public UML2WithID_SignalTrigger(
        ArrayList<UML2WithID_Signal> uml2withid_signals    ) {
        this.uml2withid_signals = uml2withid_signals;
    }


    public List<UML2WithID_Signal> getUml2withid_signals() {
        return uml2withid_signals;
    }

    public void addUml2withid_signal(Uml2withid_signal uml2withid_signal) {
        this.uml2withid_signals.add(uml2withid_signal);
    }

}