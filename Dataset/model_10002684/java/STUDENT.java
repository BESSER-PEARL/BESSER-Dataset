





import java.util.List;
import java.util.ArrayList;

public class STUDENT  {

    private String id;
    private String password;





    private List<COUNSELLOR> counsellors;


    public STUDENT(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.counsellors = new ArrayList<>();
    }

    public STUDENT(
        String id,        String password        ArrayList<COUNSELLOR> counsellors    ) {
        this.id = id;
        this.password = password;
        this.counsellors = counsellors;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<COUNSELLOR> getCounsellors() {
        return counsellors;
    }

    public void addCounsellor(Counsellor counsellor) {
        this.counsellors.add(counsellor);
    }

}