





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwIO_HwPin extends HwEndPoint {






    private HwPackage_HwPackagePin hwpackage_hwpackagepin;




    private List<HwIO_HwLine> hwio_hwlines;


    public MARTE_HwIO_HwPin(
    ) {
        super(
        );
        this.hwio_hwlines = new ArrayList<>();
    }

    public MARTE_HwIO_HwPin(
        ArrayList<HwIO_HwLine> hwio_hwlines    ) {
        this.hwio_hwlines = hwio_hwlines;
    }


    public HwPackage_HwPackagePin getHwpackage_hwpackagepin() {
        return hwpackage_hwpackagepin;
    }

    public void setHwpackage_hwpackagepin(HwPackage_HwPackagePin hwpackage_hwpackagepin) {
        this.hwpackage_hwpackagepin = hwpackage_hwpackagepin;
    }
    public List<HwIO_HwLine> getHwio_hwlines() {
        return hwio_hwlines;
    }

    public void addHwio_hwline(Hwio_hwline hwio_hwline) {
        this.hwio_hwlines.add(hwio_hwline);
    }

}