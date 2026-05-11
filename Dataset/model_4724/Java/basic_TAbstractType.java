





import java.util.List;
import java.util.ArrayList;

public class basic_TAbstractType extends TAnnotatable, TElementWithId {

    private String tName;
    private boolean tLib;





    private basic_TFieldSignature basic_tfieldsignature;




    private List<basic_TMember> basic_tmembers;




    private basic_TPackage basic_tpackage;




    private basic_TPackage basic_tpackage;




    private List<basic_TSignature> basic_tsignatures;




    private basic_TypeGraph basic_typegraph;




    private basic_TMember basic_tmember;




    private basic_TParameter basic_tparameter;




    private basic_TypeGraph basic_typegraph;


    public basic_TAbstractType(
        String tName,        boolean tLib    ) {
        super(
        );
        this.tName = tName;
        this.tLib = tLib;
        this.basic_tmembers = new ArrayList<>();
        this.basic_tsignatures = new ArrayList<>();
    }

    public basic_TAbstractType(
        String tName,        boolean tLib        ArrayList<basic_TMember> basic_tmembers,        ArrayList<basic_TSignature> basic_tsignatures    ) {
        this.tName = tName;
        this.tLib = tLib;
        this.basic_tmembers = basic_tmembers;
        this.basic_tsignatures = basic_tsignatures;
    }

    public String getTname() {
        return tName;
    }

    public void setTname(String tName) {
        this.tName = tName;
    }
    public boolean getTlib() {
        return tLib;
    }

    public void setTlib(boolean tLib) {
        this.tLib = tLib;
    }

    public basic_TFieldSignature getBasic_tfieldsignature() {
        return basic_tfieldsignature;
    }

    public void setBasic_tfieldsignature(basic_TFieldSignature basic_tfieldsignature) {
        this.basic_tfieldsignature = basic_tfieldsignature;
    }
    public List<basic_TMember> getBasic_tmembers() {
        return basic_tmembers;
    }

    public void addBasic_tmember(Basic_tmember basic_tmember) {
        this.basic_tmembers.add(basic_tmember);
    }
    public basic_TPackage getBasic_tpackage() {
        return basic_tpackage;
    }

    public void setBasic_tpackage(basic_TPackage basic_tpackage) {
        this.basic_tpackage = basic_tpackage;
    }
    public basic_TPackage getBasic_tpackage() {
        return basic_tpackage;
    }

    public void setBasic_tpackage(basic_TPackage basic_tpackage) {
        this.basic_tpackage = basic_tpackage;
    }
    public List<basic_TSignature> getBasic_tsignatures() {
        return basic_tsignatures;
    }

    public void addBasic_tsignature(Basic_tsignature basic_tsignature) {
        this.basic_tsignatures.add(basic_tsignature);
    }
    public basic_TypeGraph getBasic_typegraph() {
        return basic_typegraph;
    }

    public void setBasic_typegraph(basic_TypeGraph basic_typegraph) {
        this.basic_typegraph = basic_typegraph;
    }
    public basic_TMember getBasic_tmember() {
        return basic_tmember;
    }

    public void setBasic_tmember(basic_TMember basic_tmember) {
        this.basic_tmember = basic_tmember;
    }
    public basic_TParameter getBasic_tparameter() {
        return basic_tparameter;
    }

    public void setBasic_tparameter(basic_TParameter basic_tparameter) {
        this.basic_tparameter = basic_tparameter;
    }
    public basic_TypeGraph getBasic_typegraph() {
        return basic_typegraph;
    }

    public void setBasic_typegraph(basic_TypeGraph basic_typegraph) {
        this.basic_typegraph = basic_typegraph;
    }

}