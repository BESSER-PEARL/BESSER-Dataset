





import java.util.List;
import java.util.ArrayList;

public class Backend_CodePack_BankComponent  {






    private CodePack_Backend_CustomerHandler codepack_backend_customerhandler;




    private CodePack_Backend_ReceptionHandler codepack_backend_receptionhandler;


    public Backend_CodePack_BankComponent(
    ) {
    }



    public CodePack_Backend_CustomerHandler getCodepack_backend_customerhandler() {
        return codepack_backend_customerhandler;
    }

    public void setCodepack_backend_customerhandler(CodePack_Backend_CustomerHandler codepack_backend_customerhandler) {
        this.codepack_backend_customerhandler = codepack_backend_customerhandler;
    }
    public CodePack_Backend_ReceptionHandler getCodepack_backend_receptionhandler() {
        return codepack_backend_receptionhandler;
    }

    public void setCodepack_backend_receptionhandler(CodePack_Backend_ReceptionHandler codepack_backend_receptionhandler) {
        this.codepack_backend_receptionhandler = codepack_backend_receptionhandler;
    }

}