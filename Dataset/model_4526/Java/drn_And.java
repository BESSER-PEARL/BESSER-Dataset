





import java.util.List;
import java.util.ArrayList;

public class drn_And extends Expression {

    private String name;





    private List<drn_DepXZ_IMPL> drn_depxz_impls;




    private List<drn_DepXY_IMPL> drn_depxy_impls;




    private List<drn_DepX_Impl> drn_depx_impls;




    private List<drn_DepZ_Impl> drn_depz_impls;


    public drn_And(
        String name    ) {
        super(
        );
        this.name = name;
        this.drn_depxz_impls = new ArrayList<>();
        this.drn_depxy_impls = new ArrayList<>();
        this.drn_depx_impls = new ArrayList<>();
        this.drn_depz_impls = new ArrayList<>();
    }

    public drn_And(
        String name        ArrayList<drn_DepXZ_IMPL> drn_depxz_impls,        ArrayList<drn_DepXY_IMPL> drn_depxy_impls,        ArrayList<drn_DepX_Impl> drn_depx_impls,        ArrayList<drn_DepZ_Impl> drn_depz_impls    ) {
        this.name = name;
        this.drn_depxz_impls = drn_depxz_impls;
        this.drn_depxy_impls = drn_depxy_impls;
        this.drn_depx_impls = drn_depx_impls;
        this.drn_depz_impls = drn_depz_impls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<drn_DepXZ_IMPL> getDrn_depxz_impls() {
        return drn_depxz_impls;
    }

    public void addDrn_depxz_impl(Drn_depxz_impl drn_depxz_impl) {
        this.drn_depxz_impls.add(drn_depxz_impl);
    }
    public List<drn_DepXY_IMPL> getDrn_depxy_impls() {
        return drn_depxy_impls;
    }

    public void addDrn_depxy_impl(Drn_depxy_impl drn_depxy_impl) {
        this.drn_depxy_impls.add(drn_depxy_impl);
    }
    public List<drn_DepX_Impl> getDrn_depx_impls() {
        return drn_depx_impls;
    }

    public void addDrn_depx_impl(Drn_depx_impl drn_depx_impl) {
        this.drn_depx_impls.add(drn_depx_impl);
    }
    public List<drn_DepZ_Impl> getDrn_depz_impls() {
        return drn_depz_impls;
    }

    public void addDrn_depz_impl(Drn_depz_impl drn_depz_impl) {
        this.drn_depz_impls.add(drn_depz_impl);
    }

}