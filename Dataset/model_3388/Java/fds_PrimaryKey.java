





import java.util.List;
import java.util.ArrayList;

public class fds_PrimaryKey extends CandidateKey {






    private fds_ForeignKey fds_foreignkey;


    public fds_PrimaryKey(
    ) {
        super(
        );
    }



    public fds_ForeignKey getFds_foreignkey() {
        return fds_foreignkey;
    }

    public void setFds_foreignkey(fds_ForeignKey fds_foreignkey) {
        this.fds_foreignkey = fds_foreignkey;
    }

}