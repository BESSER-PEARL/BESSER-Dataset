





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwCommunication_HwPort extends HwEndPoint {






    private List<HwIO_HwPin> hwio_hwpins;


    public MARTE_HwCommunication_HwPort(
    ) {
        super(
        );
        this.hwio_hwpins = new ArrayList<>();
    }

    public MARTE_HwCommunication_HwPort(
        ArrayList<HwIO_HwPin> hwio_hwpins    ) {
        this.hwio_hwpins = hwio_hwpins;
    }


    public List<HwIO_HwPin> getHwio_hwpins() {
        return hwio_hwpins;
    }

    public void addHwio_hwpin(Hwio_hwpin hwio_hwpin) {
        this.hwio_hwpins.add(hwio_hwpin);
    }

}