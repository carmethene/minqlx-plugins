import minqlx

class votes(minqlx.Plugin):
    def __init__(self):
        self.add_hook("new_game", self.handle_new_game)
        self.add_command("votequestion", self.cmd_vote_question, usage="<question>", client_cmd_perm=5)
        self.add_command("votespec", self.cmd_vote_spec, usage="<id>", client_cmd_perm=0)
        self.add_command("voteready", self.cmd_vote_ready, usage="", client_cmd_perm=0)
        self.add_command("votemute", self.cmd_vote_mute, usage="", client_cmd_perm=1)
        self.add_command("voteunmute", self.cmd_vote_unmute, usage="", client_cmd_perm=1)
        self.add_command("voteabort", self.cmd_vote_abort, usage="", client_cmd_perm=2)

    def handle_new_game(self):
        minqlx.set_configstring(678, "^7:: ^1carmethene.com ^7::")
        minqlx.set_configstring(679, ":: Stats @ http://qlstats.net:8080 :: Hosted by Lindode in Fremont, CA ::")
        return

    def cmd_carmethene(self, player, msg, channel):
        player.tell("carmethene!")
        return minqlx.RET_STOP_EVENT

    def cmd_vote_question(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE

        vote_msg = " ".join(msg[1:])
        minqlx.callvote("say The players have spoken.", vote_msg, 20)
        return minqlx.RET_STOP_EVENT

    def cmd_vote_spec(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.ret_usage

        try:
            i = int(msg[1])
            target_player = self.player(i)
            if not (0 <= i < 64) or not target_player:
                raise valueerror
        except valueerror:
            channel.reply("invalid id.")
            return

        if target_player == player:
            channel.reply("i refuse.")
        else:
            minqlx.callvote("put {} s".format(target_player.id), "move {}^3 to spectators?".format(target_player.name), 20)

    def cmd_vote_ready(self, player, msg, channel):
            minqlx.callvote("allready", "all ready?", 20)

    def cmd_vote_mute(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.ret_usage

        try:
            i = int(msg[1])
            target_player = self.player(i)
            if not (0 <= i < 64) or not target_player:
                raise valueerror
        except valueerror:
            channel.reply("invalid id.")
            return

        if target_player == player:
            channel.reply("i refuse.")
        else:
            minqlx.callvote("mute {}".format(target_player.id), "mute {}^3?".format(target_player.name), 20)

    def cmd_vote_unmute(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.ret_usage

        try:
            i = int(msg[1])
            target_player = self.player(i)
            if not (0 <= i < 64) or not target_player:
                raise valueerror
        except valueerror:
            channel.reply("invalid id.")
            return

        minqlx.callvote("unmute {}".format(target_player.id), "unmute {}^3?".format(target_player.name), 20)

    def cmd_vote_abort(self, player, msg, channel):
            minqlx.callvote("abort", "abort match?", 20)

