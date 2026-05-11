




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class pokerleague_Competition extends DescribedEntity {

    private int defaultMinPlayers;
    private int defaultTournamentAnnouncementLead;
    private LocalDate endDate;
    private int defaultBuyIn;
    private LocalDate startDate;
    private int defaultMaxPlayers;
    private int minimalAttendance;





    private List<pokerleague_Player> pokerleague_players;




    private pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset;


    public pokerleague_Competition(
        int defaultMinPlayers,        int defaultTournamentAnnouncementLead,        LocalDate endDate,        int defaultBuyIn,        LocalDate startDate,        int defaultMaxPlayers,        int minimalAttendance    ) {
        super(
        );
        this.defaultMinPlayers = defaultMinPlayers;
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.endDate = endDate;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.minimalAttendance = minimalAttendance;
        this.pokerleague_players = new ArrayList<>();
    }

    public pokerleague_Competition(
        int defaultMinPlayers,        int defaultTournamentAnnouncementLead,        LocalDate endDate,        int defaultBuyIn,        LocalDate startDate,        int defaultMaxPlayers,        int minimalAttendance        ArrayList<pokerleague_Player> pokerleague_players    ) {
        this.defaultMinPlayers = defaultMinPlayers;
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.endDate = endDate;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.minimalAttendance = minimalAttendance;
        this.pokerleague_players = pokerleague_players;
    }

    public int getDefaultminplayers() {
        return defaultMinPlayers;
    }

    public void setDefaultminplayers(int defaultMinPlayers) {
        this.defaultMinPlayers = defaultMinPlayers;
    }
    public int getDefaulttournamentannouncementlead() {
        return defaultTournamentAnnouncementLead;
    }

    public void setDefaulttournamentannouncementlead(int defaultTournamentAnnouncementLead) {
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public int getDefaultbuyin() {
        return defaultBuyIn;
    }

    public void setDefaultbuyin(int defaultBuyIn) {
        this.defaultBuyIn = defaultBuyIn;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getDefaultmaxplayers() {
        return defaultMaxPlayers;
    }

    public void setDefaultmaxplayers(int defaultMaxPlayers) {
        this.defaultMaxPlayers = defaultMaxPlayers;
    }
    public int getMinimalattendance() {
        return minimalAttendance;
    }

    public void setMinimalattendance(int minimalAttendance) {
        this.minimalAttendance = minimalAttendance;
    }

    public List<pokerleague_Player> getPokerleague_players() {
        return pokerleague_players;
    }

    public void addPokerleague_player(Pokerleague_player pokerleague_player) {
        this.pokerleague_players.add(pokerleague_player);
    }
    public pokerleague_PrizeMoneyRuleSet getPokerleague_prizemoneyruleset() {
        return pokerleague_prizemoneyruleset;
    }

    public void setPokerleague_prizemoneyruleset(pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset) {
        this.pokerleague_prizemoneyruleset = pokerleague_prizemoneyruleset;
    }

}