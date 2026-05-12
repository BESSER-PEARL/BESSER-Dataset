





import java.util.List;
import java.util.ArrayList;

public class network_UsersRegistered  {

    private int serialVersionUID;





    private network_TransactionManager network_transactionmanager;


    public network_UsersRegistered(
        int serialVersionUID    ) {
        this.serialVersionUID = serialVersionUID;
    }


    public int getSerialversionuid() {
        return serialVersionUID;
    }

    public void setSerialversionuid(int serialVersionUID) {
        this.serialVersionUID = serialVersionUID;
    }

    public network_TransactionManager getNetwork_transactionmanager() {
        return network_transactionmanager;
    }

    public void setNetwork_transactionmanager(network_TransactionManager network_transactionmanager) {
        this.network_transactionmanager = network_transactionmanager;
    }

}