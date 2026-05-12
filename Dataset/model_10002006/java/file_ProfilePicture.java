





import java.util.List;
import java.util.ArrayList;

public class file_ProfilePicture  {

    private String SAVE_DIR;





    private network_TransactionManager network_transactionmanager;


    public file_ProfilePicture(
        String SAVE_DIR    ) {
        this.SAVE_DIR = SAVE_DIR;
    }


    public String getSave_dir() {
        return SAVE_DIR;
    }

    public void setSave_dir(String SAVE_DIR) {
        this.SAVE_DIR = SAVE_DIR;
    }

    public network_TransactionManager getNetwork_transactionmanager() {
        return network_transactionmanager;
    }

    public void setNetwork_transactionmanager(network_TransactionManager network_transactionmanager) {
        this.network_transactionmanager = network_transactionmanager;
    }

}