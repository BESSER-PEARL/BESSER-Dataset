





import java.util.List;
import java.util.ArrayList;

public class sipme_ObjectsFileView extends ObjectView {

    private int filePriority;
    private String fileState;





    private sipme_CompanyMember sipme_companymember;




    private sipme_CompanyMember sipme_companymember;




    private sipme_ObjectsFileView sipme_objectsfileview;




    private List<sipme_ObjectView> sipme_objectviews;


    public sipme_ObjectsFileView(
        int filePriority,        String fileState    ) {
        super(
        );
        this.filePriority = filePriority;
        this.fileState = fileState;
        this.sipme_objectviews = new ArrayList<>();
    }

    public sipme_ObjectsFileView(
        int filePriority,        String fileState        ArrayList<sipme_ObjectView> sipme_objectviews    ) {
        this.filePriority = filePriority;
        this.fileState = fileState;
        this.sipme_objectviews = sipme_objectviews;
    }

    public int getFilepriority() {
        return filePriority;
    }

    public void setFilepriority(int filePriority) {
        this.filePriority = filePriority;
    }
    public String getFilestate() {
        return fileState;
    }

    public void setFilestate(String fileState) {
        this.fileState = fileState;
    }

    public sipme_CompanyMember getSipme_companymember() {
        return sipme_companymember;
    }

    public void setSipme_companymember(sipme_CompanyMember sipme_companymember) {
        this.sipme_companymember = sipme_companymember;
    }
    public sipme_CompanyMember getSipme_companymember() {
        return sipme_companymember;
    }

    public void setSipme_companymember(sipme_CompanyMember sipme_companymember) {
        this.sipme_companymember = sipme_companymember;
    }
    public sipme_ObjectsFileView getSipme_objectsfileview() {
        return sipme_objectsfileview;
    }

    public void setSipme_objectsfileview(sipme_ObjectsFileView sipme_objectsfileview) {
        this.sipme_objectsfileview = sipme_objectsfileview;
    }
    public List<sipme_ObjectView> getSipme_objectviews() {
        return sipme_objectviews;
    }

    public void addSipme_objectview(Sipme_objectview sipme_objectview) {
        this.sipme_objectviews.add(sipme_objectview);
    }

}