





import java.util.List;
import java.util.ArrayList;

public class component_CorbaComponent extends CorbaWrapperObject, Component {

    private String rTCComponentProfile;
    private String rTCParticipationContexts;
    private String sDOOrganization;
    private String rTCRTObjects;
    private int componentState;
    private String ior;
    private String sDOConfiguration;
    private String rTCExecutionContexts;



    public component_CorbaComponent(
        String rTCComponentProfile,        String rTCParticipationContexts,        String sDOOrganization,        String rTCRTObjects,        int componentState,        String ior,        String sDOConfiguration,        String rTCExecutionContexts    ) {
        super(
        );
        this.rTCComponentProfile = rTCComponentProfile;
        this.rTCParticipationContexts = rTCParticipationContexts;
        this.sDOOrganization = sDOOrganization;
        this.rTCRTObjects = rTCRTObjects;
        this.componentState = componentState;
        this.ior = ior;
        this.sDOConfiguration = sDOConfiguration;
        this.rTCExecutionContexts = rTCExecutionContexts;
    }


    public String getRtccomponentprofile() {
        return rTCComponentProfile;
    }

    public void setRtccomponentprofile(String rTCComponentProfile) {
        this.rTCComponentProfile = rTCComponentProfile;
    }
    public String getRtcparticipationcontexts() {
        return rTCParticipationContexts;
    }

    public void setRtcparticipationcontexts(String rTCParticipationContexts) {
        this.rTCParticipationContexts = rTCParticipationContexts;
    }
    public String getSdoorganization() {
        return sDOOrganization;
    }

    public void setSdoorganization(String sDOOrganization) {
        this.sDOOrganization = sDOOrganization;
    }
    public String getRtcrtobjects() {
        return rTCRTObjects;
    }

    public void setRtcrtobjects(String rTCRTObjects) {
        this.rTCRTObjects = rTCRTObjects;
    }
    public int getComponentstate() {
        return componentState;
    }

    public void setComponentstate(int componentState) {
        this.componentState = componentState;
    }
    public String getIor() {
        return ior;
    }

    public void setIor(String ior) {
        this.ior = ior;
    }
    public String getSdoconfiguration() {
        return sDOConfiguration;
    }

    public void setSdoconfiguration(String sDOConfiguration) {
        this.sDOConfiguration = sDOConfiguration;
    }
    public String getRtcexecutioncontexts() {
        return rTCExecutionContexts;
    }

    public void setRtcexecutioncontexts(String rTCExecutionContexts) {
        this.rTCExecutionContexts = rTCExecutionContexts;
    }


}