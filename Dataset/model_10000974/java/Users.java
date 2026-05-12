





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private int Id;
    private String TwoFactorEnabled;
    private String SecurityStamp;
    private String EmailConfirmed;
    private String Email;
    private String PhoneNumber;
    private String PhoneNumberConfirmed;
    private String LockoutEndDateUtc;
    private int AccessFailedCount;
    private String PasswordHash;
    private String UserName;
    private String LockoutEnabled;



    public Users(
        int Id,        String TwoFactorEnabled,        String SecurityStamp,        String EmailConfirmed,        String Email,        String PhoneNumber,        String PhoneNumberConfirmed,        String LockoutEndDateUtc,        int AccessFailedCount,        String PasswordHash,        String UserName,        String LockoutEnabled    ) {
        this.Id = Id;
        this.TwoFactorEnabled = TwoFactorEnabled;
        this.SecurityStamp = SecurityStamp;
        this.EmailConfirmed = EmailConfirmed;
        this.Email = Email;
        this.PhoneNumber = PhoneNumber;
        this.PhoneNumberConfirmed = PhoneNumberConfirmed;
        this.LockoutEndDateUtc = LockoutEndDateUtc;
        this.AccessFailedCount = AccessFailedCount;
        this.PasswordHash = PasswordHash;
        this.UserName = UserName;
        this.LockoutEnabled = LockoutEnabled;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getTwofactorenabled() {
        return TwoFactorEnabled;
    }

    public void setTwofactorenabled(String TwoFactorEnabled) {
        this.TwoFactorEnabled = TwoFactorEnabled;
    }
    public String getSecuritystamp() {
        return SecurityStamp;
    }

    public void setSecuritystamp(String SecurityStamp) {
        this.SecurityStamp = SecurityStamp;
    }
    public String getEmailconfirmed() {
        return EmailConfirmed;
    }

    public void setEmailconfirmed(String EmailConfirmed) {
        this.EmailConfirmed = EmailConfirmed;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getPhonenumberconfirmed() {
        return PhoneNumberConfirmed;
    }

    public void setPhonenumberconfirmed(String PhoneNumberConfirmed) {
        this.PhoneNumberConfirmed = PhoneNumberConfirmed;
    }
    public String getLockoutenddateutc() {
        return LockoutEndDateUtc;
    }

    public void setLockoutenddateutc(String LockoutEndDateUtc) {
        this.LockoutEndDateUtc = LockoutEndDateUtc;
    }
    public int getAccessfailedcount() {
        return AccessFailedCount;
    }

    public void setAccessfailedcount(int AccessFailedCount) {
        this.AccessFailedCount = AccessFailedCount;
    }
    public String getPasswordhash() {
        return PasswordHash;
    }

    public void setPasswordhash(String PasswordHash) {
        this.PasswordHash = PasswordHash;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getLockoutenabled() {
        return LockoutEnabled;
    }

    public void setLockoutenabled(String LockoutEnabled) {
        this.LockoutEnabled = LockoutEnabled;
    }


}