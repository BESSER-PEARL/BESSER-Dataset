





import java.util.List;
import java.util.ArrayList;

public class USER  {

    private boolean verified;
    private String createdAt;
    private String _id;
    private String email;
    private String surname;
    private String telephone;
    private String address;
    private String password;
    private String updateAt;
    private String lastAccess;
    private String name;
    private String status;



    public USER(
        boolean verified,        String createdAt,        String _id,        String email,        String surname,        String telephone,        String address,        String password,        String updateAt,        String lastAccess,        String name,        String status    ) {
        this.verified = verified;
        this.createdAt = createdAt;
        this._id = _id;
        this.email = email;
        this.surname = surname;
        this.telephone = telephone;
        this.address = address;
        this.password = password;
        this.updateAt = updateAt;
        this.lastAccess = lastAccess;
        this.name = name;
        this.status = status;
    }


    public boolean getVerified() {
        return verified;
    }

    public void setVerified(boolean verified) {
        this.verified = verified;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUpdateat() {
        return updateAt;
    }

    public void setUpdateat(String updateAt) {
        this.updateAt = updateAt;
    }
    public String getLastaccess() {
        return lastAccess;
    }

    public void setLastaccess(String lastAccess) {
        this.lastAccess = lastAccess;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}