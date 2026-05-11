





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_FeatureDecl extends Decl {






    private List<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls;




    private List<deviceModelingLanguage_Assignment> devicemodelinglanguage_assignments;




    private deviceModelingLanguage_Exp devicemodelinglanguage_exp;




    private deviceModelingLanguage_Device devicemodelinglanguage_device;




    private List<deviceModelingLanguage_Device> devicemodelinglanguage_devices;




    private deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl;


    public deviceModelingLanguage_FeatureDecl(
    ) {
        super(
        );
        this.devicemodelinglanguage_memberdecls = new ArrayList<>();
        this.devicemodelinglanguage_assignments = new ArrayList<>();
        this.devicemodelinglanguage_devices = new ArrayList<>();
    }

    public deviceModelingLanguage_FeatureDecl(
        ArrayList<deviceModelingLanguage_MemberDecl> devicemodelinglanguage_memberdecls,        ArrayList<deviceModelingLanguage_Assignment> devicemodelinglanguage_assignments,        ArrayList<deviceModelingLanguage_Device> devicemodelinglanguage_devices    ) {
        this.devicemodelinglanguage_memberdecls = devicemodelinglanguage_memberdecls;
        this.devicemodelinglanguage_assignments = devicemodelinglanguage_assignments;
        this.devicemodelinglanguage_devices = devicemodelinglanguage_devices;
    }


    public List<deviceModelingLanguage_MemberDecl> getDevicemodelinglanguage_memberdecls() {
        return devicemodelinglanguage_memberdecls;
    }

    public void addDevicemodelinglanguage_memberdecl(Devicemodelinglanguage_memberdecl devicemodelinglanguage_memberdecl) {
        this.devicemodelinglanguage_memberdecls.add(devicemodelinglanguage_memberdecl);
    }
    public List<deviceModelingLanguage_Assignment> getDevicemodelinglanguage_assignments() {
        return devicemodelinglanguage_assignments;
    }

    public void addDevicemodelinglanguage_assignment(Devicemodelinglanguage_assignment devicemodelinglanguage_assignment) {
        this.devicemodelinglanguage_assignments.add(devicemodelinglanguage_assignment);
    }
    public deviceModelingLanguage_Exp getDevicemodelinglanguage_exp() {
        return devicemodelinglanguage_exp;
    }

    public void setDevicemodelinglanguage_exp(deviceModelingLanguage_Exp devicemodelinglanguage_exp) {
        this.devicemodelinglanguage_exp = devicemodelinglanguage_exp;
    }
    public deviceModelingLanguage_Device getDevicemodelinglanguage_device() {
        return devicemodelinglanguage_device;
    }

    public void setDevicemodelinglanguage_device(deviceModelingLanguage_Device devicemodelinglanguage_device) {
        this.devicemodelinglanguage_device = devicemodelinglanguage_device;
    }
    public List<deviceModelingLanguage_Device> getDevicemodelinglanguage_devices() {
        return devicemodelinglanguage_devices;
    }

    public void addDevicemodelinglanguage_device(Devicemodelinglanguage_device devicemodelinglanguage_device) {
        this.devicemodelinglanguage_devices.add(devicemodelinglanguage_device);
    }
    public deviceModelingLanguage_FeatureDecl getDevicemodelinglanguage_featuredecl() {
        return devicemodelinglanguage_featuredecl;
    }

    public void setDevicemodelinglanguage_featuredecl(deviceModelingLanguage_FeatureDecl devicemodelinglanguage_featuredecl) {
        this.devicemodelinglanguage_featuredecl = devicemodelinglanguage_featuredecl;
    }

}