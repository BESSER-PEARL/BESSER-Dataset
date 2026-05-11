





import java.util.List;
import java.util.ArrayList;

public class raspirover_RasPiBoard extends Board {






    private List<raspirover_AnalogPin> raspirover_analogpins;




    private List<raspirover_DigitalPin> raspirover_digitalpins;


    public raspirover_RasPiBoard(
    ) {
        super(
        );
        this.raspirover_analogpins = new ArrayList<>();
        this.raspirover_digitalpins = new ArrayList<>();
    }

    public raspirover_RasPiBoard(
        ArrayList<raspirover_AnalogPin> raspirover_analogpins,        ArrayList<raspirover_DigitalPin> raspirover_digitalpins    ) {
        this.raspirover_analogpins = raspirover_analogpins;
        this.raspirover_digitalpins = raspirover_digitalpins;
    }


    public List<raspirover_AnalogPin> getRaspirover_analogpins() {
        return raspirover_analogpins;
    }

    public void addRaspirover_analogpin(Raspirover_analogpin raspirover_analogpin) {
        this.raspirover_analogpins.add(raspirover_analogpin);
    }
    public List<raspirover_DigitalPin> getRaspirover_digitalpins() {
        return raspirover_digitalpins;
    }

    public void addRaspirover_digitalpin(Raspirover_digitalpin raspirover_digitalpin) {
        this.raspirover_digitalpins.add(raspirover_digitalpin);
    }

}