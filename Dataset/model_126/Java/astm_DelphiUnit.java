





import java.util.List;
import java.util.ArrayList;

public class astm_DelphiUnit extends CompilationUnit {






    private astm_Name astm_name;




    private astm_DelphiInterfaceSection astm_delphiinterfacesection;




    private astm_DelphiImplementationSection astm_delphiimplementationsection;


    public astm_DelphiUnit(
    ) {
        super(
        );
    }



    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }
    public astm_DelphiInterfaceSection getAstm_delphiinterfacesection() {
        return astm_delphiinterfacesection;
    }

    public void setAstm_delphiinterfacesection(astm_DelphiInterfaceSection astm_delphiinterfacesection) {
        this.astm_delphiinterfacesection = astm_delphiinterfacesection;
    }
    public astm_DelphiImplementationSection getAstm_delphiimplementationsection() {
        return astm_delphiimplementationsection;
    }

    public void setAstm_delphiimplementationsection(astm_DelphiImplementationSection astm_delphiimplementationsection) {
        this.astm_delphiimplementationsection = astm_delphiimplementationsection;
    }

}