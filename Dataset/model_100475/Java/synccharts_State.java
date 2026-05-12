





import java.util.List;
import java.util.ArrayList;

public class synccharts_State extends Scope {

    private String type;
    private boolean isInitial;
    private boolean isFinal;





    private synccharts_Region synccharts_region;




    private synccharts_Region synccharts_region;




    private List<synccharts_Region> synccharts_regions;




    private synccharts_Region synccharts_region;


    public synccharts_State(
        String type,        boolean isInitial,        boolean isFinal    ) {
        super(
        );
        this.type = type;
        this.isInitial = isInitial;
        this.isFinal = isFinal;
        this.synccharts_regions = new ArrayList<>();
    }

    public synccharts_State(
        String type,        boolean isInitial,        boolean isFinal        ArrayList<synccharts_Region> synccharts_regions    ) {
        this.type = type;
        this.isInitial = isInitial;
        this.isFinal = isFinal;
        this.synccharts_regions = synccharts_regions;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public synccharts_Region getSynccharts_region() {
        return synccharts_region;
    }

    public void setSynccharts_region(synccharts_Region synccharts_region) {
        this.synccharts_region = synccharts_region;
    }
    public synccharts_Region getSynccharts_region() {
        return synccharts_region;
    }

    public void setSynccharts_region(synccharts_Region synccharts_region) {
        this.synccharts_region = synccharts_region;
    }
    public List<synccharts_Region> getSynccharts_regions() {
        return synccharts_regions;
    }

    public void addSynccharts_region(Synccharts_region synccharts_region) {
        this.synccharts_regions.add(synccharts_region);
    }
    public synccharts_Region getSynccharts_region() {
        return synccharts_region;
    }

    public void setSynccharts_region(synccharts_Region synccharts_region) {
        this.synccharts_region = synccharts_region;
    }

}