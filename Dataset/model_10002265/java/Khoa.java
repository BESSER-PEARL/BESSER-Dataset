





import java.util.List;
import java.util.ArrayList;

public class Khoa  {

    private String tenkhoa;
    private String makhoa;





    private List<BoMon> bomons;


    public Khoa(
        String tenkhoa,        String makhoa    ) {
        this.tenkhoa = tenkhoa;
        this.makhoa = makhoa;
        this.bomons = new ArrayList<>();
    }

    public Khoa(
        String tenkhoa,        String makhoa        ArrayList<BoMon> bomons    ) {
        this.tenkhoa = tenkhoa;
        this.makhoa = makhoa;
        this.bomons = bomons;
    }

    public String getTenkhoa() {
        return tenkhoa;
    }

    public void setTenkhoa(String tenkhoa) {
        this.tenkhoa = tenkhoa;
    }
    public String getMakhoa() {
        return makhoa;
    }

    public void setMakhoa(String makhoa) {
        this.makhoa = makhoa;
    }

    public List<BoMon> getBomons() {
        return bomons;
    }

    public void addBomon(Bomon bomon) {
        this.bomons.add(bomon);
    }

}