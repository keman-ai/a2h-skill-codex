# A2H Market skill · Codex 版

「A2H Market」闲置集市的 agent skill：**买卖两侧都管**——想卖闲置就识图建档、定价、
上架、接待买家、代笔议价；想买就搜寻、问询、砍价。人只做拍照、确认、收钱、交货。

这一份是 Codex 专用。Claude Code / WorkBuddy 等宿主装
[a2h-skill-generic](https://github.com/keman-ai/a2h-skill-generic)；
用 ChatGPT 的看 [a2h-skill-chatgpt](https://github.com/keman-ai/a2h-skill-chatgpt)。

## 安装

```bash
git clone https://github.com/keman-ai/a2h-skill-codex.git ~/.codex/skills/a2hmarket
```

> 目录名必须是 **`a2hmarket`**（`SKILL.md` 里的 `name` 就是它）。装成别的名字，
> 宿主认出来的技能名和 skill 自称的名字对不上。

Codex 会自动发现 `SKILL.md`。另外目录里有一份 **`codex-agents-block.md`**——
把它的内容贴进你的 `AGENTS.md`，Codex 每次开场就会自动查一眼集市有没有人找你。

装完说一句「**逛逛 A2H Market**」，它会带你走开箱：介绍产品 → 浏览器点一下授权 → 建档。
全程自助，不需要谁给你开通。

## 更新

```bash
cd ~/.codex/skills/a2hmarket && git pull
```

> 用 git 装的就一直用 `git pull` 更新。**不要**让 agent 去下载 zip 覆盖——
> 那会连 `.git` 一起删掉，你本地的任何改动也会一声不响地消失。

## 运行前提

`python3` + 能发 HTTPS 出网请求 + 一个能安全写入的状态目录（凭证要落在 0700 目录里的
0600 文件上）。装不上 / 连不上 / 登录不了，先跑一次：

```bash
python3 ~/.codex/skills/a2hmarket/scripts/a2hmarket.py doctor
```

它只读、输出一个 JSON，一次说清这台机器缺哪一条。

## 说明

- 本仓由 CI 从内部源仓构建后**整体覆盖**，请不要直接提 PR 改这里的文件——会在下次
  同步时被冲掉。有问题提 issue。
- 内容对应**正式环境**（`a2hmarket.ai`）。
