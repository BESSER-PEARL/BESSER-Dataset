





import java.util.List;
import java.util.ArrayList;

public class patronrecord  {

    private String dateofmembership;
    private String address;
    private String patronid;
    private String name;
    private String phone_no;
    private String filesowned;
    private String noofbooks_alooted;
    private String type;





    private patron patron;


    public patronrecord(
        String dateofmembership,        String address,        String patronid,        String name,        String phone_no,        String filesowned,        String noofbooks_alooted,        String type    ) {
        this.dateofmembership = dateofmembership;
        this.address = address;
        this.patronid = patronid;
        this.name = name;
        this.phone_no = phone_no;
        this.filesowned = filesowned;
        this.noofbooks_alooted = noofbooks_alooted;
        this.type = type;
    }


    public String getDateofmembership() {
        return dateofmembership;
    }

    public void setDateofmembership(String dateofmembership) {
        this.dateofmembership = dateofmembership;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPatronid() {
        return patronid;
    }

    public void setPatronid(String patronid) {
        this.patronid = patronid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(String phone_no) {
        this.phone_no = phone_no;
    }
    public String getFilesowned() {
        return filesowned;
    }

    public void setFilesowned(String filesowned) {
        this.filesowned = filesowned;
    }
    public String getNoofbooks_alooted() {
        return noofbooks_alooted;
    }

    public void setNoofbooks_alooted(String noofbooks_alooted) {
        this.noofbooks_alooted = noofbooks_alooted;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public patron getPatron() {
        return patron;
    }

    public void setPatron(patron patron) {
        this.patron = patron;
    }

}