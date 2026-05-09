





import java.util.List;
import java.util.ArrayList;

public class pycom_Function extends ExpMember {






    private pycom_Board pycom_board;




    private pycom_Import pycom_import;


    public pycom_Function(
    ) {
        super(
        );
    }



    public pycom_Board getPycom_board() {
        return pycom_board;
    }

    public void setPycom_board(pycom_Board pycom_board) {
        this.pycom_board = pycom_board;
    }
    public pycom_Import getPycom_import() {
        return pycom_import;
    }

    public void setPycom_import(pycom_Import pycom_import) {
        this.pycom_import = pycom_import;
    }

}