





import java.util.List;
import java.util.ArrayList;

public class drn_And extends Movement {

    private String name;





    private List<drn_DepX_Impl> drn_depx_impls;




    private List<drn_DepY_Impl> drn_depy_impls;




    private List<drn_Rotate> drn_rotates;




    private List<drn_DepZ_Impl> drn_depz_impls;


    public drn_And(
        String name    ) {
        super(
        );
        this.name = name;
        this.drn_depx_impls = new ArrayList<>();
        this.drn_depy_impls = new ArrayList<>();
        this.drn_rotates = new ArrayList<>();
        this.drn_depz_impls = new ArrayList<>();
    }

    public drn_And(
        String name        ArrayList<drn_DepX_Impl> drn_depx_impls,        ArrayList<drn_DepY_Impl> drn_depy_impls,        ArrayList<drn_Rotate> drn_rotates,        ArrayList<drn_DepZ_Impl> drn_depz_impls    ) {
        this.name = name;
        this.drn_depx_impls = drn_depx_impls;
        this.drn_depy_impls = drn_depy_impls;
        this.drn_rotates = drn_rotates;
        this.drn_depz_impls = drn_depz_impls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<drn_DepX_Impl> getDrn_depx_impls() {
        return drn_depx_impls;
    }

    public void addDrn_depx_impl(Drn_depx_impl drn_depx_impl) {
        this.drn_depx_impls.add(drn_depx_impl);
    }
    public List<drn_DepY_Impl> getDrn_depy_impls() {
        return drn_depy_impls;
    }

    public void addDrn_depy_impl(Drn_depy_impl drn_depy_impl) {
        this.drn_depy_impls.add(drn_depy_impl);
    }
    public List<drn_Rotate> getDrn_rotates() {
        return drn_rotates;
    }

    public void addDrn_rotate(Drn_rotate drn_rotate) {
        this.drn_rotates.add(drn_rotate);
    }
    public List<drn_DepZ_Impl> getDrn_depz_impls() {
        return drn_depz_impls;
    }

    public void addDrn_depz_impl(Drn_depz_impl drn_depz_impl) {
        this.drn_depz_impls.add(drn_depz_impl);
    }

}